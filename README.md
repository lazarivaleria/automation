# Individual Work 05 – Ansible Playbooks

## 1. Project Description

The objective of this individual work was to learn how to create Ansible playbooks for automating server configuration.

The project uses Docker, Docker Compose, Jenkins, Ansible, Apache2, PHP and SSH.

Four containers were created:
- Jenkins Controller – manages automation pipelines.
- SSH Agent – builds and tests the PHP application.
- Ansible Agent – executes Ansible playbooks.
- Test Server – hosts the deployed PHP application.

## 2. Jenkins Controller Configuration

I created a Jenkins Controller service in the `compose.yaml` file.

I launched the container using Docker Compose and accessed Jenkins through `http://localhost:8081`.

I installed the required plugins:
- Docker
- Docker Pipeline
- GitHub Integration
- SSH Agent
- SSH Build Agents
- Pipeline
- JUnit

I also configured SSH credentials to allow Jenkins to communicate with its agents.

## 3. SSH Agent Configuration

I created the `Dockerfile.ssh_agent` file based on Ubuntu.

I installed PHP CLI, Composer, Java, Git and OpenSSH Server.

I created an SSH key pair and configured the public key on the SSH Agent. The private key was added to Jenkins credentials.

I configured the SSH Agent as a Jenkins node with the label `php-agent`.

## 4. Ansible Agent Configuration

I created the `Dockerfile.ansible_agent` file based on Ubuntu.

I installed Ansible, Python, Java, Git and OpenSSH Server.

I configured SSH authentication between Jenkins and the Ansible Agent.

I also created a separate SSH key pair for communication between the Ansible Agent and the Test Server.

The Ansible Agent connects to the Test Server using the `ansible` user.

## 5. Test Server Configuration

I created the `Dockerfile.test_server` file based on Ubuntu.

I installed OpenSSH Server and created the `ansible` user.

I configured SSH key authentication and granted the user permission to execute administrative commands.

The Test Server was added to the Docker network and exposed on port 8082 for HTTP access.

## 6. Ansible Playbook Description

I created the `ansible` folder containing `hosts.ini`, `ansible.cfg` and `setup_test_server.yml`.

The playbook performs the following tasks:

1. Updates the package list.
2. Installs Apache2.
3. Installs PHP and the required extensions.
4. Enables the Apache rewrite module.
5. Creates the project directory.
6. Configures an Apache virtual host.
7. Enables the virtual host and disables the default one.
8. Starts and enables the Apache service.

I also created `deploy_php.yml` to transfer the PHP application to the Test Server.

## 7. Jenkins Pipelines

I created three Jenkins pipelines.

### 7.1. PHP Build and Test Pipeline

The `php_build_and_test_pipeline.groovy` pipeline:
- Clones the GitHub repository.
- Installs dependencies using Composer.
- Executes unit tests using PHPUnit.
- Publishes test results using JUnit.

### 7.2. Ansible Setup Pipeline

The `ansible_setup_pipeline.groovy` pipeline:
- Clones the repository.
- Executes the `setup_test_server.yml` playbook.
- Configures Apache2 and PHP on the Test Server.

### 7.3. PHP Deploy Pipeline

The `php_deploy_pipeline.groovy` pipeline:
- Clones the repository.
- Executes the deployment playbook.
- Copies the PHP project to the Test Server.
- Restarts Apache2.

## 8. Testing

I executed all three Jenkins pipelines.

After configuring the server and deploying the application, I accessed `http://localhost:8082` in the browser.

The application was displayed successfully, confirming that Apache2 and PHP were configured correctly.

## 9. Questions and Answers

### 9.1. What are the advantages of using Ansible for server configuration?

Ansible provides several advantages:
- Automation of repetitive configuration tasks.
- Simple YAML syntax.
- No need to install an agent on remote servers.
- SSH-based communication.
- Consistent configuration across multiple servers.
- Idempotency, meaning that repeated executions do not unnecessarily change an already correct configuration.

### 9.2. What other Ansible modules exist for configuration management?

Some commonly used Ansible modules are:

- `apt` – installs and manages packages on Debian and Ubuntu.
- `yum` and `dnf` – manage packages on RPM-based systems.
- `service` – manages system services.
- `systemd` – manages systemd services.
- `copy` – copies files to remote servers.
- `file` – manages files, directories and permissions.
- `user` – creates and manages users.
- `group` – manages user groups.
- `template` – generates configuration files using Jinja2 templates.
- `lineinfile` – modifies specific lines in configuration files.
- `authorized_key` – manages SSH authorized keys.

### 9.3. What problems did you encounter when creating the Ansible playbook and how did you solve them?

During the implementation, I encountered several configuration challenges.

One problem was configuring SSH authentication between the Ansible Agent and the Test Server. I solved it by generating a separate SSH key pair and adding the public key to the `ansible` user's authorized keys.

Another challenge was configuring the correct inventory parameters. I solved it by specifying the Test Server hostname, SSH port, user and private key path in `hosts.ini`.

I also had to configure the Apache virtual host and the correct project directory. I solved this by using Ansible tasks to create the directory, configure the virtual host and restart Apache.

## 10. Conclusion

During this individual work, I learned how to automate server configuration using Ansible playbooks and integrate them into Jenkins pipelines.

I created separate agents for PHP testing and Ansible automation, configured a test server and deployed a PHP application.

The final result demonstrated how Docker, Jenkins and Ansible can work together to automate the build, testing, configuration and deployment processes.