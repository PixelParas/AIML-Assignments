import random
import time

class GridEnvironment:
    def __init__(self, size=4, initial_dirt_chance=0.3, new_dirt_chance=0.05):
        self.size = size
        self.initial_dirt_chance = initial_dirt_chance
        self.new_dirt_chance = new_dirt_chance
        self.reset()

    def reset(self):
        """Starts a new episode by regenerating the 2D grid."""
        # 2D Array: 0 means Clean, 1 means Dirty
        self.grid = [
            [1 if random.random() < self.initial_dirt_chance else 0 for _ in range(self.size)]
            for _ in range(self.size)
        ]
        # Place agent at a random starting coordinate (x, y)
        self.agent_pos = [random.randint(0, self.size - 1), random.randint(0, self.size - 1)]
        self.steps_taken = 0

    def get_percept(self):
        """The agent only perceives if its current square is dirty."""
        x, y = self.agent_pos
        is_dirty = self.grid[y][x] == 1
        return is_dirty

    def is_fully_clean(self):
        """Checks if the episode is over (grid is 100% clean)."""
        return all(self.grid[y][x] == 0 for y in range(self.size) for x in range(self.size))

    def execute_action(self, action):
        """Updates the environment based on the agent's action."""
        x, y = self.agent_pos
        self.steps_taken += 1

        if action == 'Suck':
            self.grid[y][x] = 0
        elif action == 'Up' and y > 0:
            self.agent_pos[1] -= 1
        elif action == 'Down' and y < self.size - 1:
            self.agent_pos[1] += 1
        elif action == 'Left' and x > 0:
            self.agent_pos[0] -= 1
        elif action == 'Right' and x < self.size - 1:
            self.agent_pos[0] += 1
        # If it hits a wall, the position simply doesn't change.

        # DYNAMIC ENVIRONMENT: Random chance for new dirt to appear anywhere
        if random.random() < self.new_dirt_chance:
            rx, ry = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.grid[ry][rx] = 1

    def display(self):
        """Prints a visual representation of the 2D array."""
        for y in range(self.size):
            row_str = ""
            for x in range(self.size):
                if [x, y] == self.agent_pos:
                    row_str += "[A] "  # Agent
                elif self.grid[y][x] == 1:
                    row_str += " *  "  # Dirt
                else:
                    row_str += " .  "  # Clean floor
            print(row_str)
        print("-" * 20)


class StochasticReflexAgent:
    def act(self, is_dirty):
        # Condition-Action Rule 1: If dirty, always suck
        if is_dirty:
            return 'Suck'
        # Condition-Action Rule 2: If clean, move randomly (Stochastic element)
        else:
            return random.choice(['Up', 'Down', 'Left', 'Right'])


def run_episodes(num_episodes=2, max_steps=50):
    env = GridEnvironment(size=4) # 4x4 Grid
    agent = StochasticReflexAgent()

    for episode in range(1, num_episodes + 1):
        print(f"\n{'='*30}\nSTARTING EPISODE {episode}\n{'='*30}")
        env.reset()
        
        for step in range(1, max_steps + 1):
            print(f"Step {step}:")
            env.display()
            
            # Check for episode completion
            if env.is_fully_clean():
                print(f"🎉 Episode {episode} finished! The room is fully clean in {env.steps_taken} steps.")
                break
                
            # Agent perceives and acts
            percept_dirty = env.get_percept()
            action = agent.act(percept_dirty)
            
            print(f"Agent Action: {action}\n")
            env.execute_action(action)
            
            # Add a tiny pause so it's easier to read if running in a real terminal
            time.sleep(0.1)
            
        else:
            print(f"⚠️ Episode {episode} ended. Reached max steps ({max_steps}) before cleaning everything.")

if __name__ == "__main__":
    run_episodes(num_episodes=2, max_steps=40)mport random
import time

class GridEnvironment:
    def __init__(self, size=4, initial_dirt_chance=0.3, new_dirt_chance=0.05):
        self.size = size
        self.initial_dirt_chance = initial_dirt_chance
        self.new_dirt_chance = new_dirt_chance
        self.reset()

    def reset(self):
        """Starts a new episode by regenerating the 2D grid."""
        # 2D Array: 0 means Clean, 1 means Dirty
        self.grid = [
            [1 if random.random() < self.initial_dirt_chance else 0 for _ in range(self.size)]
            for _ in range(self.size)
        ]
        # Place agent at a random starting coordinate (x, y)
        self.agent_pos = [random.randint(0, self.size - 1), random.randint(0, self.size - 1)]
        self.steps_taken = 0

    def get_percept(self):
        """The agent only perceives if its current square is dirty."""
        x, y = self.agent_pos
        is_dirty = self.grid[y][x] == 1
        return is_dirty

    def is_fully_clean(self):
        """Checks if the episode is over (grid is 100% clean)."""
        return all(self.grid[y][x] == 0 for y in range(self.size) for x in range(self.size))

    def execute_action(self, action):
        """Updates the environment based on the agent's action."""
        x, y = self.agent_pos
        self.steps_taken += 1

        if action == 'Suck':
            self.grid[y][x] = 0
        elif action == 'Up' and y > 0:
            self.agent_pos[1] -= 1
        elif action == 'Down' and y < self.size - 1:
            self.agent_pos[1] += 1
        elif action == 'Left' and x > 0:
            self.agent_pos[0] -= 1
        elif action == 'Right' and x < self.size - 1:
            self.agent_pos[0] += 1
        # If it hits a wall, the position simply doesn't change.

        # DYNAMIC ENVIRONMENT: Random chance for new dirt to appear anywhere
        if random.random() < self.new_dirt_chance:
            rx, ry = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.grid[ry][rx] = 1

    def display(self):
        """Prints a visual representation of the 2D array."""
        for y in range(self.size):
            row_str = ""
            for x in range(self.size):
                if [x, y] == self.agent_pos:
                    row_str += "[A] "  # Agent
                elif self.grid[y][x] == 1:
                    row_str += " *  "  # Dirt
                else:
                    row_str += " .  "  # Clean floor
            print(row_str)
        print("-" * 20)


class StochasticReflexAgent:
    def act(self, is_dirty):
        # Condition-Action Rule 1: If dirty, always suck
        if is_dirty:
            return 'Suck'
        # Condition-Action Rule 2: If clean, move randomly (Stochastic element)
        else:
            return random.choice(['Up', 'Down', 'Left', 'Right'])


def run_episodes(num_episodes=2, max_steps=50):
    env = GridEnvironment(size=4) # 4x4 Grid
    agent = StochasticReflexAgent()

    for episode in range(1, num_episodes + 1):
        print(f"\n{'='*30}\nSTARTING EPISODE {episode}\n{'='*30}")
        env.reset()
        
        for step in range(1, max_steps + 1):
            print(f"Step {step}:")
            env.display()
            
            # Check for episode completion
            if env.is_fully_clean():
                print(f"🎉 Episode {episode} finished! The room is fully clean in {env.steps_taken} steps.")
                break
                
            # Agent perceives and acts
            percept_dirty = env.get_percept()
            action = agent.act(percept_dirty)
            
            print(f"Agent Action: {action}\n")
            env.execute_action(action)
            
            # Add a tiny pause so it's easier to read if running in a real terminal
            time.sleep(0.1)
            
        else:
            print(f"⚠️ Episode {episode} ended. Reached max steps ({max_steps}) before cleaning everything.")

if __name__ == "__main__":
    run_episodes(num_episodes=2, max_steps=40)
