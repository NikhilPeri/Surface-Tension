# Writing A Routine
A routine is a sequece of movements that are run in order to animate the wall. once deployed to the
pi it will automatically be run the next time someone interacts with the wall.

1. Start by dulicating the [sample_routine](../routines/sample_routine.py) to your own file, you can name it
anything just be sure to use lower case undescore convention so it can be imported as a python module.
2. Now you can implement any motion in the `run` method using a combination of [Wall Commands](./wall_api.md) and
`time.sleep` to introduce delays.  The run routine will receive a wall in the fully retracted position.
3. When you done just run `pytest` to ensure that the new routine will run as expected.  If the test pass you can open a PR
