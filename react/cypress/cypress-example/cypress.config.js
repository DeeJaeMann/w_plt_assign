import { defineConfig } from 'cypress';

export default defineConfig({
    e2e: {
        baseUrl: "http://localhost:5173",
        supportFile: false,
        specPattern: "cypress/e2e/**/*.cy.{js,jsx,tx,tsx}"
    },
    viewportWidth: 1024,
    viewportHeight: 768,
    video: false
})