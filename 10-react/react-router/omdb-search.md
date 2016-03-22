#OMDB Search Functionality

Now to get the search feature working. We'll need a couple functions in order to correctly search for a movie.

* `searchChange`, to update the value of the input field
* `search`, to take the `searchTerm` and query OMDB

Let's make these changes in `src/components/OMDBSearch.jsx`

```js
const React = require('react');

const OMDBSearch = React.createClass({
  getInitialState: function() {
    return {searchTerm: '', results: []};
  },
  searchChange: function(e) {
    this.setState({searchTerm: e.target.value});
  },
  search: function(e) {
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
  },
  render: function() {
    return (
      <div>
        <h1>Search for Movies</h1>
        <form onSubmit={this.search}>
          <input type="text"
                 value={this.state.searchTerm}
                 onChange={this.searchChange} />
          <input type="submit" />
        </form>
      </div>
    );
  }
});

module.exports = OMDBSearch;
```

Much of this is similar to the Todo app from before, but what's with this `fetch` function. Where did it come from?

`fetch` is a new and experimental interface for interacting with network resources. It's similar to AJAX, only it's available natively in some browsers. Note that this will only work in later versions of Chrome and Firefox, but there are scripts called **polyfills** that allow you to use this feature in all browsers.

* [Documentation for fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* [window.fetch polyfill](https://github.com/github/fetch)

After testing the code above, there should be search results appearing in the console. Now for rendering...

###Rendering Search Results

To make things simpler, we're going to render the search results directly in the `OMDBSearch` component, without making a separate component. Let's modify the `render` function to do this.

```js
render: function() {
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

###Passing imdbIDs to ShowMovie

To link correctly to the `ShowMovie` components, we'll need a `react-router` module called `Link` in order to create the links. In `/src/components/OMDBSearch.jsx`, let's require the `Link` module.

```js
const Link = require('react-router').Link;
```

Then, we'll create the `Link` components inside of the `render` function. This will allow us to create links and pass the imdbIDs to the `ShowMovie` component.

```js
render: function() {
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

###Rendering Movie Details

In order to render movie details, we'll need to fetch the data in a similar manner as `OMDBSearch`. Our workflow will look like so:

* Set the initial state of the movie to `null` while we search for the movie
  * If the movie doesn't exist, display **Loading** to the page
* Search for the movie using the `imdbID` passed via route params
  * Once the data is found, set the movie state
* Render the movie to the page

In `MovieShow`, let's add the following:

```js
const React = require('react');
const Link = require('react-router').Link;

const ShowMovie = React.createClass({
  getInitialState() {
    return {movie: null};
  },
  componentDidMount() {
    fetch(`http://omdbapi.com/?i=${this.props.params.imdbID}`)
      .then(response => {
        response.json().then(data => {
          this.setState({movie: data});
        });
      }).catch(error => {
        this.setState({movie: null});
      });
  },
  render: function() {
    const movie = this.state.movie;
    if (!movie) return <h1>Loading...</h1>;

    return (
      <div>
        <h1>{movie.Title}</h1>
        <p>{movie.Plot}</p>
        <Link to='/'>&larr; Back</Link>
      </div>
    );
  }
});

module.exports = ShowMovie;
```

We should now have a working movie app, complete with a **Back** button via `Link`.
