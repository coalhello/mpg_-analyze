import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "auto-mpg.csv"
df = pd.read_csv(file_path)

fig, axes = plt.subplots(1, 4, figsize=(20, 5))  # 4개의 그래프를 배치

# 실린더 수 vs MPG
sns.boxplot(x=df["cylinders"], y=df["mpg"], ax=axes[0])
axes[0].set_title("MPG vs Cylinders")

# 배기량 vs MPG
sns.scatterplot(x=df["displacement"], y=df["mpg"], alpha=0.6, ax=axes[1])
axes[1].set_title("MPG vs Displacement")

# 무게 vs MPG
sns.scatterplot(x=df["weight"], y=df["mpg"], alpha=0.6, ax=axes[2])
axes[2].set_title("MPG vs Weight")

# 가속 vs MPG
sns.scatterplot(x=df["mpg"], y=df["acceleration"], alpha=0.6, ax=axes[3])
sns.regplot(x=df["mpg"], y=df["acceleration"], scatter=False, color="red", ax=axes[3])
axes[3].set_title("MPG vs Acceleration")

plt.tight_layout()
plt.show()
