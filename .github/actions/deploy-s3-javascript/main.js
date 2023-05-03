// We import the installed dependenceis, see below

const core = require('@actions/core');
const giithbu = require('@actions/github');
const exec = require('@actions/exec');

function run() {
    core.notice('Hello from my custom JavaScrio action.'); // this will log a message in the gh log.
}

//  in order to communicate with gh we need to install in the actions folder
//  npm install @actions/core @actions/github @actions/exec
// we need to push the files under node_modules, produced with the install. As they'll be needed for theexecution.
run();