![Build Status](https://dev.azure.com/odluser234198/AzureDevOps/_apis/build/status%2Fnqthien041292.Ensuring-Quality-Releases-Project?branchName=main)

# Overview

This document presents the final project "Ensuring Quality Releases" for Udacity.

# Project Structure

- **azure-pipelines.yaml**: This file contains Azure Pipelines YAML configurations.
- **automatedtesting**: This directory contains suites of different tests:
  - **jmeter**: Load test files including JMeterPlan.jmx, CSV inputs, and TestReports (endurance-report, stress-report).
  - **postman**: Functional test files in Postman collections and environments.
  - **selenium**: UI tests implemented in uitests.py.
- **screenshots**: This folder contains various screenshot requests.
- **terraform**: Terraform scripts used for Infrastructure as Code (IaC).

## Environment Creation & Deployment

### Terraform Infrastructure Deployment

We use Terraform to apply Infrastructure as Code (IaC). Below are screenshots of the log output of Terraform when executed by the CI/CD pipeline:

- ![Resources Created by Terraform](screenshots/az-resource-created.png)
- ![Terraform Execution in Pipelines (Success)](screenshots/devops-pipelines-01.png)
- ![Terraform State](screenshots/az-container.png)

### Automated Testing Tasks

Here, we provide a screenshot of the successful execution of the pipeline build results page (`/_build/results?buildId={id}&view=results`):

- ![Complete Final Pipeline](screenshots/devops-execute-success-01.png)

## Automated Testing

### Load Test Suite

The following are screenshots of the log output of JMeter when executed by the CI/CD pipeline:

- ![Load Test Result 1](screenshots/devops-test-jmeter-stress.png)
- ![Load Test Result 2](screenshots/devops-test-jmeter-endurance.png)

### Functional Test Suites

Here's a screenshot of the execution of the test suite by the CI/CD pipeline:

- ![Functional Test Result](screenshots/devops-test-selenium-ui.png)

### API-Integration Tests

- Screenshot of the output of the Publish Test Results step:
  - ![Publish Test Results](screenshots/devops-test-postman-01.png)

- Screenshot of the Run Summary page, which contains four graphs:
  - ![Test Report Summary](screenshots/devops-test-postman-02.png)

- Screenshot of the Test Results page, which contains the test case titles from each test:
  - ![Test Report Results](screenshots/devops-test-postman-03.png)

## Monitoring & Observability

### Configure Azure Monitor

Here are screenshots of the graphs of the resource when the alert was triggered:

- ![Alert Summary](screenshots/az-appservice-log-1.png)

And here's a screenshot of the alert rule:

- ![Alert Rule](screenshots/az-appservice-log-2.png)

Additionally, we have screenshots related to AppService alerts:

- ![AppService Alerts](screenshots/az-appservice-log.png)

Finally, there are screenshots of the email received when the alert is triggered:

- ![Alert Email](screenshots/az-log-email.png)

### Azure Log Analytics

Screenshots of log analytics queries and result sets, which show specific output of the Azure resource:

- ![Log Analytics Queries](screenshots/az-log-1.png)
