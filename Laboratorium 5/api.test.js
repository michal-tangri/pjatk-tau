/**
 * @jest-environment node
 */

const api = require('./api');

/* Podpunkt: "niepoprawny request" */
it('fails with status code 403 when bad endpoint is called', () => {
    return expect(api.sendGetRequest('spatny_pozadavek')).rejects.toThrow('Request failed with status code 403');
});

/* Podpunkt: "zawartość poprawnego requestu - czy istnieje" */
it('returns response data when correct request is sent', () => {
    return api.getCasesByCountry('Germany').then(response => expect(response.data).toBeDefined());
});

/* Podpunkt: "zawartość konkretnych wartośći (req -> /country=Poland res -> country: Poland)" */
it('returns current number of cases for Germany', () => {
    return api.getCasesByCountry('Germany').then(response => expect(response.data['All'].capital_city).toBe('Berlin'));
});

/* Podpunkt: "zwartość contentu -> klucze" */
it('returns current number of cases for Germany and contains data about Baden-Wurttemberg', () => {
    return api.getCasesByCountry('Germany').then(response => expect(response.data).toHaveProperty('Baden-Wurttemberg'));
});
