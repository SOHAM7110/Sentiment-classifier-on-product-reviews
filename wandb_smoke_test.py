import wandb

run = wandb.init(project="review-sentiment", name="setup-smoke-test", config={"seed": 42})
for step in range(10):
    wandb.log({"dummy_loss": 1 / (step + 1), "step": step})
wandb.finish()