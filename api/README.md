# Simple Node with Express Server with REST API

An easy way to get started with a Express server offering a REST API with Node.js.

## Features

- Express
- REST API

## Requirements

- [node & npm](https://nodejs.org/en/)
- [git](https://www.robinwieruch.de/git-essential-commands/)

## Installation

- `npm install`
- `npm start`
- optional: include _.env_ in your _.gitignore_

##  Endpoints


### GET

- visit http://localhost:3000
  - /messages
  - /messages/1


### CREATE

- Create a message with:
  - `curl -X POST -H "Content-Type:application/json" http://localhost:3000/messages -d '{"text":"Hi again, World"}'`

### DELETE

- Delete a message with:
  - `curl -X DELETE -H "Content-Type:application/json" http://localhost:3000/messages/1`
