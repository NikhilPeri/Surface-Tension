# Surface-Tension
This is the code that powers the living wall art installation at the University of Ottawa STEM Complex.


## How To Contribute
1. Take a look at the [Wall API](docs/wall_api.md) and some of the [existing routines](routines) in the project.
2. There is a [How to Guide](docs/routines.md) availible Write a routine to animate the wall and place it in the `routines/` directory.
3. Once your code has been reviewed and merged to master you can ssh into the pi and run the `scripts/deploy` from the project directory
this will update and reboot the pi to run the new code.
