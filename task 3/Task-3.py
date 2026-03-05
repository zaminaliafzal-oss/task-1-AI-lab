class ModelBasedReflexAgent:
    def __init__(self, threshold=20):
        self.threshold = threshold
        self.heater_on = False
        self.previous_action = None
    def perceive(self, temperature):
        """
        Decide action based on current temperature and previous action.
        Avoid turning heater on/off unnecessarily.
        """
        if temperature < self.threshold:
            if self.previous_action != "heater_on":
                self.heater_on = True
                self.previous_action = "heater_on"
                return "Turn heater ON"
            else:
                return "Heater already ON, no action"
        else:
            if self.previous_action != "heater_off":
                self.heater_on = False
                self.previous_action = "heater_off"
                return "Turn heater OFF"
            else:
                return "Heater already OFF, no action"
agent = ModelBasedReflexAgent(threshold=20)
temperatures = [18, 19, 20, 21, 19, 18, 22, 23]
for temp in temperatures:
    action = agent.perceive(temp)
    print(f"Temperature: {temp}°C -> {action}")