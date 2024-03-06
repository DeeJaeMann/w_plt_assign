// React init test

describe('Testing React initialization', () => {
    it('Visits the app and asserts title', () => {
        cy.visit('/');
        cy.get('h1').should('contain', 'Vite + React');
    });
});