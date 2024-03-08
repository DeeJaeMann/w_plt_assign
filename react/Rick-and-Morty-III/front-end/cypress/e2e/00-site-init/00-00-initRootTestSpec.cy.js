describe('00-00 Test initial site root elements', () => {

    it('00 - Visits the app and asserts title in h1 element', () => {
        cy.visit('/');
        cy.get('h1')
            .invoke('text')
            .should('match', /(rick)*(morty)*/gi);
    });
})