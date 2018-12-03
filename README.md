# Jacks-Car-Rental
The implementation of Jack's Car Rental problem in the "Reinforcement Learning (2018) Second Edition" book by Sutton and Barto, MIT Press publication. Used Tabular Q-Learning method to solve the task, using number of cars at each location as states, and moving the number of cars between the locations as actions. If unfamiliar with the problem, that is as follows:

`Jack’s Car Rental Jack manages two locations for a nationwide car rental company. Each day, some number of customers arrive at each location to rent cars. If Jack has a car available, he rents it out and is credited $10 by the national company. If he is out of cars at that location, then the business is lost. Cars become available for renting the day after they are returned. To help ensure that cars are available where they are needed, Jack can move them between the two locations overnight, at a cost of $2 per car moved. We assume that the number of cars requested and returned at each location are Poisson random variables, meaning that the probability that the number is n is λ^n * e^(−λ) / n!, where λ is the expected number. Suppose λ is 3 and 4 for rental requests at the first and second locations and 3 and 2 for returns. To simplify the problem slightly, we assume that there can be no more than 20 cars at each location (any additional cars are returned to the nationwide company, and thus disappear from the problem) and a maximum of five cars can be moved from one location to the other in one night. We take the discount rate to be γ = 0.9 and formulate this as a continuing finite MDP, where the time steps are days, the state is the number of cars at each location at the end of the day, and the actions are the net numbers of cars moved between the two locations overnight.`

My choice of rewards is as follows:

`+n for renting where n is the number of cars rented from both locations.
-n for the deficiency of cars than what was requested for rent at both locations.
The total of these 2 values is the reward for that state-action pair in my implementation.`

Value of lambda is as defined to be used in the problem.
