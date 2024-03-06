import { defineConfig } from 'cypress';

export default defineConfig({
    e2e: {
        baseUrl: "http://localhost:5173/",
        supportFile: false,
    },

    component: {
        devServer: {
            framework: 'react',
            bundler: 'vite'
        },
        supportFile: false,
        specPattern: "./cypress/component/**/*.cy.{js,jsx,ts,tsx}",
    },
    viewportWidth: 1024,
    viewportHeight: 768,
    video: false,
})