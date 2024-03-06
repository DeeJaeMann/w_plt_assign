describe('Test initial base HTML elements', () => {

  it('01 - Visits the app and asserts title', () => {
    cy.visit('/');
    cy.get('h1').should('contain', 'Hangman');
  });

  it('02 - Test for puzzle word display to have no letters', () => {
    cy.visit('/');
    cy.get('.puzzleText')
      .invoke('text')
      .should('match', /Puzzle: [^a-z]/gi);
  });

  it('03 - Test for message requesting user to guess a letter', () => {
    cy.visit('/');
    cy.get('form')
      .find('span')
      .invoke('text')
      .should('match', /(guess)*(letter)*/gi );
  });

  it('04 - Test if the input field is type text', () => {
    cy.visit('/');
    cy.get('form')
      .find('input')
      .invoke('attr', 'type')
      .should('contain', 'text');
  });

  it('05 - Test if the input field has 1 character max size', () => {
    cy.visit('/');
    cy.get('form')
      .find('input')
      .invoke('attr', 'maxLength')
      .should('contain', '1');
  });

  it('06 - Test if the text typed in input matches the displayed text', () => {
    cy.visit('/');
    cy.get('form')
      .find('input')
      .type('a')
      .invoke('attr', 'value')
      .should('contain', 'a');
  })
})