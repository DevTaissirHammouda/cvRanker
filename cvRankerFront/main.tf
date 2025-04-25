# Specify the provider as Docker
provider "docker" {}

# Define a Docker image resource
resource "docker_image" "devops" {
  name = "devops"

  build {
    context = "${path.module}"  # Path to your application directory (current directory)
    dockerfile = "Dockerfile"    # Make sure the Dockerfile is in the same directory
  }
}

# Define a Docker container resource
resource "docker_container" "devops" {
  name  = "devops"               # Name for the Docker container
  image = docker_image.devops.latest  # Reference to the built image

  ports {
    internal = 5000  # Port inside the container
    external = 5000  # Port exposed on the host machine
  }
}
