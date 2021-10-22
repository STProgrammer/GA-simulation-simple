The starter code consists of 3 python files: GAengine.py, Main.py and Utils.py. 
You will need to install pygame in your environment for the code to work.
Main.py contains the render code. The initial population is also created here. 

GAengine.py will contain the bulk of your genetic algorithm implementation. 
There are skeleton functions in place for fitness assignment and selection.
Utils.py contains helper classes. GAPoint is a simple class representing a 
position in the world, with a function to find the distance to another GAPoint. 
Chromosome represents the chromosome and has skeleton functions for crossover 
and mutation. The chromosome only has two features, the x and y position of the 
individual in the world, used for rendering the individual in the simulator. 
They are already implemented using high-level representation in the class GAPoint.
