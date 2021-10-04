# OMDB Search

Now to get the search feature working. We'll need a couple functions in order to correctly search for a movie.

* `searchChange`, to update the value of the input field
* `search`, to take the `searchTerm` and query OMDB

Let's make these changes in `src/components/OMDBSearch.jsx`

```javascript
import React, { Component } from 'react';
import Navbar from './Navbar';
import MovieResult from './MovieResult';

class OMDBSearch extends Component {
  constructor() {
    super();
    this.state = {
      searchTerm: '',
      results: []
    };
  }
  searchChange (e) {
    this.setState({searchTerm: e.target.value});
  }
  search (e) {
    console.log("searching");
    e.preventDefault();
    fetch(`http://omdbapi.com/?s=${this.state.searchTerm}`)
      .then(response => {
        response.json().then(data => {
          console.log(data.Search);
          this.setState({results: data.Search});
        });
      }).catch(error => {
        this.setState({results: null});
      });
  }
  render () {
    return (
      <div>
        <Navbar />
        <h1>Search for Movies</h1>
        <form onSubmit={(e) => this.search(e)}>
          <input type="text"
                 value={this.state.searchTerm}
                 onChange={(e) => this.searchChange(e)} />
          <input type="submit" />
        </form>
        {this.results()}
      </div>
    );
  }

  results() {
    return this.state.results.map(result =>
      <MovieResult title={result.Title}
                   year={result.Year}
                   poster={result.Poster}
                   imdbID={result.imdbID} />
    );
  }
}

module.exports = OMDBSearch;
```

Much of this is similar to the Todo app from before, but what's with this `fetch` function. Where did it come from?

`fetch` is a new and experimental interface for interacting with network resources. It's similar to AJAX, only it's available natively in some browsers. Note that this will only work in later versions of Chrome and Firefox, but there are scripts called **polyfills** that allow you to use this feature in all browsers.

* [Documentation for fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* [window.fetch polyfill](https://github.com/github/fetch)

After testing the code above, there should be search results appearing in the console. Now for rendering...

## Rendering Search Results

To make things simpler, we're going to render the search results directly in the `OMDBSearch` component, without making a separate component. Let's modify the `render` function to do this.

```javascript
render () {
  const results = this.state.results.map((movie, idx) => {
    return (
      <div className="well" key={idx}>
        <h2>{movie.Title}</h2>
        <p>imdbID: {movie.imdbID}</p>
      </div>
    );
  });

  return (
    <div>
      <h1>Search for Movies</h1>
      <form onSubmit={this.search}>
        <input type="text"
               value={this.state.searchTerm}
               onChange={this.searchChange} />
        <input type="submit" />
      </form>
      <div>{results}</div>
    </div>
  );
}
```

## Passing imdbIDs to ShowMovie

To link correctly to the `ShowMovie` components, we'll need a `react-router` module called `Link` in order to create the links. In `/src/components/OMDBSearch.jsx`, let's require the `Link` module.

```javascript
const Link = require('react-router').Link;
```

Then, we'll create the `Link` components inside of the `render` function. This will allow us to create links and pass the imdbIDs to the `ShowMovie` component.

```javascript
render () {
  const results = this.state.results.map((movie, idx) => {
    return (
      <div className="well" key={idx}>
        <h2><Link to={`/results/${movie.imdbID}`} >{movie.Title}</Link></h2>
      </div>
    );
  });

  return (
    <div>
      <h1>Search for Movies</h1>
      <form onSubmit={this.search}>
        <input type="text"
               value={this.state.searchTerm}
               onChange={this.searchChange} />
        <input type="submit" />
      </form>
      <div>{results}</div>
    </div>
  );
}
```

Test the app again by searching for a movie and clicking on one of the links. We should be redirected to the `ShowMovie` component, where the imdbID is rendered to the page.

## Rendering Movie Details

In order to render movie details, we'll need to fetch the data in a similar manner as `OMDBSearch`. Our workflow will look like so:

* Set the initial state of the movie to `null` while we search for the movie
  * If the movie doesn't exist, display **Loading** to the page
* Search for the movie using the `imdbID` passed via route params
  * Once the data is found, set the movie state
* Render the movie to the page

In `MovieShow`, let's add the following:

```javascript
import React, { Component } from 'react';
import Navbar from './Navbar'

class ShowMovie extends Component {
  constructor(props) {
    super(props);

    this.state = {
      movie: null
    }

    fetch(`http://omdbapi.com/?i=${this.props.params.imdbID}`)
    .then(response => {
      console.log("got response:", response);
      response.json().then(data => {
        this.setState({movie: data});
      });
    }).catch(error => {
      console.log("error");
      this.setState({movie: null});
    });
  }

  render() {
    const movie = this.state.movie;
    if (!movie) {
      return <div>
        <Navbar />
        <h2>Loading...</h2>
      </div>
    }

    return (
      <div>
        <Navbar />
        <h2>({movie.Year}) {movie.Title}</h2>
        <img src={movie.Poster} />
        <p>
          {movie.Plot}
        </p>
      </div>
    );
  }
}

export default ShowMovie;
```

We should now have a working movie app, complete with a **Back** button via `Link`.

