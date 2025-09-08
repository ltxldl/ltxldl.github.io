# Serving Lectures

This directory contains lecture slides written with Reveal.js that can be served via either GitHub Pages or a local web server.

## Serving Locally (Recommended for Development)

Serving the slides locally allows several advantages, such as the ability to see **speaker notes** and **automatic reloading** when you make changes to the slides.

1. Install Node.js.
1. Go to this directory in your terminal and run `npm install` to install dependencies.
1. Serve the presentation by running `npm start`.
1. Open your web browser and navigate to http://localhost:8000 to view the slides.

## Serving via GitHub Pages

Nothing special is needed. Just push your changes to the `main` branch, and GitHub Pages will automatically serve the content.

# Createing New Lectures

1. Copy `lecture-template.html` to a new file named `lecture-xxx-title.html`, where `xxx` is the lecture number (e.g., `001`, `002`, etc.) and `title` is a short description of the lecture topic (e.g., `introduction`, `data-processing`, etc.).
1. Edit the new file to update the lecture title, date, and content.
1. Commit and push the new file to the repository.
