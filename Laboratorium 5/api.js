const axios = require('axios');

function sendGetRequest(endpoint) {
    return axios.get(`https://covid-api.mmediagroup.fr/v1/${endpoint}`);
};

function getCasesByCountry(country) {
    return axios.get(`https://covid-api.mmediagroup.fr/v1/cases?country=${country}`);
}

module.exports = {
    sendGetRequest,
    getCasesByCountry,
};