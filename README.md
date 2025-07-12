# GitHub Actions Docker Build Demo

This is a simple demo project showing how to create a GitHub Actions workflow that builds a Docker image and can be triggered manually via the GitHub CLI.

## Project Structure

```
.
├── app.py                          # Simple Python Hello World app
├── Dockerfile                      # Docker configuration
├── .github/workflows/docker-build.yml  # GitHub Actions workflow
└── README.md                       # This file
```

## Prerequisites

1. **GitHub CLI** - Install from [cli.github.com](https://cli.github.com/)
2. **Git** - For cloning and pushing to GitHub
3. **GitHub Account** - To create the repository

## Setup Instructions

### 1. Create GitHub Repository

```bash
# Create a new repository on GitHub
gh repo create github-actions-docker-demo --public

# Clone the repository
git clone https://github.com/YOUR_USERNAME/github-actions-docker-demo.git
cd github-actions-docker-demo
```

### 2. Add Project Files

Copy all the files from this demo project to your repository:

```bash
# Add all files
git add .
git commit -m "Initial commit: Add GitHub Actions Docker workflow demo"
git push origin main
```

### 3. Trigger the Workflow

You can trigger the workflow manually using the GitHub CLI:

```bash
# Basic workflow run
gh workflow run docker-build.yml

# With custom tag
gh workflow run docker-build.yml -f tag=v1.0.0

# Check workflow status
gh run list --workflow=docker-build.yml
```

### 4. View Logs and Output

To view the workflow logs:

```bash
# List recent runs
gh run list --workflow=docker-build.yml

# View logs for the most recent run
gh run view --log

# View logs for a specific run ID
gh run view RUN_ID --log
```

You can also view the logs in the GitHub web interface:
1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. Click on the "Docker Build Workflow" workflow
4. Click on the specific run to see detailed logs

## Workflow Features

- **Manual Trigger**: Uses `workflow_dispatch` to allow manual triggering
- **Docker Build**: Builds a Docker image from the Dockerfile
- **Container Testing**: Runs the container to verify it works
- **Build Logs**: Shows detailed build output in GitHub Actions interface
- **Custom Tags**: Allows specifying custom Docker image tags

## Sample Output

When you run the workflow, you'll see output like:

```
🐳 Building Docker image...
✅ Docker image built successfully!
📋 Available Docker images:
🧪 Testing Docker container...
🐳 Hello from Docker!
Current time: 2024-01-15 10:30:45.123456
Python version: 3.11.x
This is a simple demo app for GitHub Actions Docker workflow
Application started successfully!
✅ Container test completed!
📊 Build Summary:
- Image: demo-app:latest
- Build completed at: Mon Jan 15 10:30:45 UTC 2024
- Workflow triggered by: your-username
```

## Customization

- **Change the app**: Edit `app.py` to modify the application
- **Modify Docker setup**: Update `Dockerfile` for different base images or configurations
- **Extend workflow**: Add steps to the `.github/workflows/docker-build.yml` file
- **Add triggers**: Include other triggers like `push` or `pull_request` in the workflow

## Troubleshooting

If the workflow fails:

1. Check the logs using `gh run view --log`
2. Verify all files are properly committed to the repository
3. Ensure the workflow file is in the correct location: `.github/workflows/docker-build.yml`
4. Make sure Docker syntax is correct in the Dockerfile 