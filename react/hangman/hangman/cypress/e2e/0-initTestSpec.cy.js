describe('Test base HTML elements', () => {
  it('Visits the app and asserts title', () => {
    cy.visit('/')
    cy.get('h1').should('contain', 'Hangman');
  })
})