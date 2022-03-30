# Netlify

Netlify is PaaS (Platform as a Service) that provides a simple workflow for deploying react apps, and even when using the free tier of Netlify, your react app will serve up bery quickly (no more waiting for Heroku dynos to spinn up 🥴). Netlify cannot be used to deploy an express server in a meaningful way, so your backeend should be deployed to somewhere else in a 'Decoupled App' setup.

When using Netlify to deploy our React frontend, this frontend will be our Client that must make backend API calls.

1. (if you are working in a team) -- At this point, double check that your own personal repo is up to date with the main git repo for your team, and that all your own personal most recent work has been committed and merged into the main git repo. 
  * once your client repo is up to date, checkout to a deployment branch
2. **If you currently have any non-breaking React errors on the terminal when you deploy the frontend:** We have to let Netlify know we are okay with these. Netlify, by default, is not. Longterm, you will want to correct all these errors and then undo the next bit of instructions, but for deployment today do the following. In your `package.json` on the frontend, replace the current `"build": "react-scripts-build",` with `"build": "CI= react-scripts build",`. Commit and push your changes. 
3. Use your Github to sign up for Netlify [here](https://www.netlify.com/).
4. After login, on your dashboard, click "New site from Git" in the top right hand corner. 
5. Under "Continuous Deployment" click "Github", and authorize Netlify to access your Github repositories. 
6. Under "Deploy settings" leave as default, and 
7. To add environmental variables (like your `REACT_APP_SERVER_URL`) click on the "Advanced options" above the Deploy button, then click the "Add variable" button. This should look a lot like the Heroku site. Add your variables and press deploy!
8. Netlify will take several minutes to build the app; check in with a Dev if there are any bugs. 

A few things to note:

- Netlify's environmental variables are set on deploy—if your variable changes, you'll need to trigger a redeploy to make that change go into effect.Instructions for how to deploy decoupled MERN apps using MongoDB Atlas, Heroku, and Netlify. 

## Common bugs

Sometimes when using then `react-router-dom` package, you will receive a 'Page Not Found' error when navigating to some of your routes. 

Never fear! We can resolve the issue easily by adding `_redirects` to the `/public` folder of your react app with instructions on where routes redirect `/*    index.html   200`

* touch `./public/_redirects`
* add `/*    index.html   200` to `./public/_redirects`
* git add, commit and push on your deployed branch, and wait for Netlify to build again 



