var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, './MovieLens/movielens/static/scripts/js/');
var APP_DIR = path.resolve(__dirname, './MovieLens/movielens/static/scripts/jsx/');

var config = {
  entry: {
    login:APP_DIR+"/login",
    register:APP_DIR+"/register",
    pointAllocation:APP_DIR+"/point_allocation",
    recommendation:APP_DIR+"/recommendation",
    landingPage: APP_DIR+"/landingPage",
    movieDetail:APP_DIR+"/movieDetail",
    home:APP_DIR+"/home",
    similarMovie:APP_DIR+"/similarMovie"
  },
  output: {
    path: BUILD_DIR,
    filename: '[name].js',
  },
    module : {
    loaders : [
      {
          exclude: /node_modules/,
          test: /\.jsx?/,
          include: APP_DIR,
          loader: 'babel'
      }
    ]
  }

};

module.exports = config;