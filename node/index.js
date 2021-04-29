const { Client } = require('pg');

const faker = require('faker');

const config = require('./dbconfig.json');

const client = new Client({
	user : config.user,
	host : config.host,
	database : config.dbname,
	password : config.password,
	port : config.port,
});

faker.seed(10);

let spotify_data = [];

for (var i = 0; i<10; i++) {
	var _id = i
	var _genre = faker.music.genre();
	var _artist = faker.name.findName();
	var _album = faker.random.word();
	let spotify_obj = {
		id : _id,
		genre : _genre,
		artist : _artist,
		album : _album
	}

	spotify_data.push(spotify_obj);
}

const values = (data) => {
	let values = "";

	let row = {};

	for(var i=0; i<data.length; i++) {
		row = data[i];
		row.artist = row.artist.replace("'", "''");
		values += `(\'${row.genre}\', \'${row.artist}\', \'${row.album}\')`;
		if (i == data.length-1) {
			values += ";";
		}
		else {
			values += ',';
		}
	}
	return values
}


create = `CREATE TABLE IF NOT EXISTS public.spotify(id SERIAL PRIMARY KEY, genre VARCHAR(15), artist VARCHAR(30), album VARCHAR(20))`;
const statement = `INSERT INTO spotify(genre, artist, album) VALUES`;
const vals = values(spotify_data);
const insert = statement + vals;
console.log(insert);

client.connect()
.then(()=> console.log("Connected"))
.then(()=> client.query(create))
.then(()=> client.query(insert))
.catch(err=> console.log(err))
.finally(()=> client.end());




