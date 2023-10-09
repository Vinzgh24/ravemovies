const axios = require('axios');

async function fetchMovieGenres() {
  try {
    const response = await axios.get('https://api.themoviedb.org/3/genre/movie/list', {
      params: {
        api_key: 'ea0c8bc1b7235d9e19b457c965b658ad',
      },
    });
    return response.data.genres;
  } catch (error) {
    console.error(error);
    return [];
  }
}

module.exports = fetchMovieGenres;
