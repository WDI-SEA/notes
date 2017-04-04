# Noise Algorithms

- Explain the basic idea of a noise algorithm versus completely random number generation
- Describe some applications of noise algorithms
- Describe the difference between Simplex and Perlin noise

### What is a noise algorithm?

A noise algorithm is a way to generate a series of random values which are somewhat tied to the previously generated values. Some practical applications include cheaply (in terms of memory/processing) generating terrain in a video game, or other more natural-looking phenomena, such as flames or clouds.

Let's say we're generating a series of number from 1 to 10. Complete randomness might look like:

`4, 10, 1, 8, 2, 2, 9, 3, 6, 1, 9, 8, 5, 1, 10, 2`

Notice the numbers may be close together or far apart. Meanwhile, a noise algorithm might generate numbers more like the following:

`3, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 7, 8, 7, 6, 5`

It is 'randomish', but each value is tied to the previous value whereas a truly random number is completely separate from it's previous values. If you're flipping a coin and have had heads come up 9 times in a row, what are the odds that the 10th flip will be tails? Still 50%. Trippy, but that is true randomness!

### What is Perlin noise?

Let's watch this video to get started
[Perlin Noise](https://www.youtube.com/watch?v=Qf4dIN99e2w)

[Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise) is sometimes referred to as "classic noise". The inventor of Perlin noise algorithm, [Ken Perlin](https://en.wikipedia.org/wiki/Ken_Perlin) invented the algorithm in 1983 after working on the original Tron movie (released in 1982). He thought that computer generated graphics at the time were too rigid and machine-like.

This algorithm's complexity is O(2^n), where n is the number of dimensions.

### What is Simplex noise?

The [Simplex noise](https://en.wikipedia.org/wiki/Simplex_noise) was also designed by Ken Perlin, nearly two decades after his original noise algorithm. It has a lower computational overhead than Perlin noise, and scales more easily to higher dimensions. It's complexity is O(n^2) for n dimensions. 

Our code will only deal with two dimensions for today, but it is important to know that these algorithms can be applied to any number of dimensions.

## Implementation

### Complete randomness

First, let's take a look at what a texture generated completely randomly looks like. Notice the stark contrasts!

`Plug Starter Code`

Notice that the constrasts are not smooth.

## Resources
- [How to use Perlin Noise in your Games](http://devmag.org.za/2009/04/25/perlin-noise/)

