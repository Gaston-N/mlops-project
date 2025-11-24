package main

import (
	"context"
	"fmt"

	"dagger.io/dagger"
)

func main() {
	ctx := context.Background()

	if err := executeBuild(ctx); err != nil {
		fmt.Println("Error:", err)
		panic(err)
	}
}

func executeBuild(ctx context.Context) error {
	client, err := dagger.Connect(ctx)
	if err != nil {
		return fmt.Errorf("error: failed to connect to Dagger client: %w", err)
	}
	defer client.Close()

	projectPath := "/mlops-project"

	pythonContainer := client.Container().From("python:3.12.2-bookworm").
		WithDirectory(projectPath, client.Host().Directory(".")).
		WithWorkdir(projectPath)

	commands := [][]string{
		{"pip", "install", "dvc"},
		{"dvc", "init", "-f"},
		{"make", "requirements"},
		{"make", "setup"},
		{"make", "data"},
		{"python", projectPath + "/src/preprocessing.py"},
		{"python", projectPath + "/src/modeling/train.py"},
		{"python", projectPath + "/src/modeling/model_select.py"},
		{"python", projectPath + "/src/modeling/model_deploy.py"},
	}

	for _, cmd := range commands {
		pythonContainer = pythonContainer.WithExec(cmd)
	}

	if _, err := pythonContainer.Directory(projectPath+"/data/processed").Export(ctx, "output"); err != nil {
		return fmt.Errorf("failed to export artifacts: %w", err)
	}

	return nil
}
