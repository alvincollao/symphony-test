# symphony-test
test environment to familiarize the github command.

## Table of Contents

- [Change log](#change-log)
- [Development Setup](#development-setup)
  - [Installation](#installation)
  - [Running Tests](#running-tests)
  - [Code Quality](#code-quality)
- [Testing Configuration](#testing-config)
- [Exporting Manifests](#exporting-manifests)
- [Running the Operator](#running-operator)
- [Installing the operator to GKE](SYMPHONY_GKE_INSTALL.md)

## <a id="change-log"></a>Change log

### Version 0.2.6
- Added initial pod status check on operator startup to ensure existing pods are accounted
  for in status updates.

### Version 0.2.5
- Exposed option to enable/disable preemption handling logic. Defaulted to false.
- Exposed labels and taints variables to allow the user to specify a list of labels
  to identify VMs in the cluster that can be preempted by Google Compute Engine, and
  taints that would indicate a VM is being preempted.
  
####
Modify by Ronald

####

Modify 2/18/2016


#####

Modify by Ron through cli
