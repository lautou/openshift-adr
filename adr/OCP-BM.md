# ARCHITECTURE DECISION RECORDS FOR: OpenShift Container Platform - Specifics of baremetal installation

## OCP-BM-01

**Title**
OCP installation method on baremetal infrastructure

**Architectural Question**
Which OCP installation method will be used to deploy a cluster on baremetal infrastructure?

**Issue or Problem**
The choice of installation method for Bare Metal impacts the level of automation, network prerequisites (like PXE), and how the cluster interacts with the physical hardware.

**Assumption**
N/A

**Alternatives**

- User-Provisioned Infrastructure (UPI)
- Installer-Provisioned Infrastructure (IPI)
- Agent-based Installer (ABI)
- Assisted Installer

**Decision**
#TODO: Document the decision for the Bare Metal cluster.#

**Justification**

- **User-Provisioned Infrastructure (UPI):** Requires the user to manually configure and manage networking, DNS, load balancers, and provisioning of RHCOS onto bare metal hosts prior to installation.
- **Installer-Provisioned Infrastructure (IPI):** Automates host provisioning and networking by leveraging Bare Metal Operator (BMO) features, suitable if metal resources are fully automated via BMO.
- **Agent-based Installer (ABI):** Uses discovery ISOs and a lightweight agent to gather hardware information, simplifying installation for both connected and disconnected bare metal environments.
- **Assisted Installer:** A web-based SaaS service designed to generate installation artifacts and manage the installation process, offering a simplified user experience for bare metal deployments.

**Implications**

- **User-Provisioned Infrastructure (UPI):** Highest operational overhead and responsibility for day 1/2 operations.
- **Installer-Provisioned Infrastructure (IPI):** Requires integration with BMO and related provisioning infrastructure. Allows use of Machine API for lifecycle management.
- **Agent-based Installer (ABI):** Highly flexible for restricted networks and provides integrated tools for configuring nodes (e.g., LVM storage configuration).
- **Assisted Installer:** Requires a working internet connection during the preparation phase (unless run disconnected). Simplifies deployment by handling Ignition configuration generation.

  **Agreeing Parties**

- Person: #TODO#, Role: Enterprise Architect
- Person: #TODO#, Role: OCP Platform Owner
- Person: #TODO#, Role: Infra Leader

---

## OCP-BM-02

**Title**
Bare Metal Node Remediation

**Architectural Question**
What is the strategy for automatically remediating unhealthy Bare Metal nodes?

**Issue or Problem**
A strategy is needed to automatically detect and recover failed physical nodes. This is critical for maintaining cluster health and HA for workloads, especially for stateful services that run directly on the nodes.

**Assumption**
N/A.

**Alternatives**

- No Automated Remediation
- Node Health Check (NHC) with Self Node Remediation
- Node Health Check (NHC) with BareMetal Operator (BMO) Remediation

**Decision**
#TODO: Document the decision for the Bare Metal cluster.#

**Justification**

- **No Automated Remediation:** To rely on manual detection (via monitoring) and manual intervention by an operator to troubleshoot and reboot physical nodes.
- **Node Health Check (NHC) with Self Node Remediation:** To deploy the Node Health Check operator, which monitors node health. When a node fails, the `SelfNodeRemediation` agent on other nodes will fence the unhealthy node and restart its workloads elsewhere.
- **Node Health Check (NHC) with BareMetal Operator (BMO) Remediation:** To use the NHC in combination with the BareMetal Operator (enabled by an IPI install). When NHC detects a failure, it triggers the BMO to power-cycle the node via its BMC, attempting a full hardware reboot.

**Implications**

- **No Automated Remediation:** High operational burden and slow recovery times. Not recommended for a production cluster.
- **Node Health Check (NHC) with Self Node Remediation:** Provides software-level remediation. It ensures workloads are moved but does not fix the underlying node, which will remain unavailable until manually repaired.
- **Node Health Check (NHC) with BareMetal Operator (BMO) Remediation:** This is the most robust, fully automated solution. It attempts to recover the node by "turning it off and on again" via its BMC. This requires a reliable IPI installation and stable Redfish/IPMI connectivity. Furthermore, the BMO facilitates the **Cluster API management of compute nodes (TP)** for dynamic lifecycle management. Advanced operational features, such as performing **live updates to HostFirmwareSettings (TP)** or **HostFirmwareComponents (TP)**, are available through BMO, but utilizing live updates requires setting the **HostUpdatePolicy (TP)** resource to `onReboot`. **We do not recommend that you perform live updates to the BMC on OpenShift Container Platform 4.20 for test purposes, especially on earlier generation hardware**

**Agreeing Parties**

- Person: #TODO#, Role: Enterprise Architect
- Person: #TODO#, Role: OCP Platform Owner
- Person: #TODO#, Role: Infra Leader

## OCP-BM-03

**Title**
Kernel Module and Device Plugin Management on Bare Metal using KMM

**Architectural Question**
What standard mechanism will be used to build, deploy, and manage out-of-tree kernel modules (like specialized GPU or NIC drivers) and their corresponding device plugins across bare metal cluster nodes?

**Issue or Problem**
Specialized hardware acceleration or networking components often require kernel modules and device plugins not included in the default Red Hat Enterprise Linux CoreOS (RHCOS) images. Deploying these manually leads to version misalignment and complex lifecycle management whenever kernel updates occur.

**Assumption**
The bare metal cluster will utilize specialized hardware requiring out-of-tree kernel drivers (e.g., GPUs or high-performance network adapters).

**Alternatives**

- Kernel Module Management (KMM) Operator
- Manual build and DaemonSet deployment (Driver Toolkit approach)

**Justification**

- **Kernel Module Management (KMM) Operator:** KMM is designed to simplify the lifecycle management of kernel modules by automating the build process, tracking kernel versions, and optionally signing the resulting kernel objects.
- **Manual build and DaemonSet deployment (Driver Toolkit approach):** This method requires manually fetching the Driver Toolkit image, building the module outside the cluster, and creating DaemonSets for deployment and pre/post-start hooks. This is highly complex and error-prone during RHCOS updates.

**Implications**

- **Kernel Module Management (KMM) Operator:** Requires installing and maintaining the KMM Operator and associated secrets/config maps. Provides high operational stability by ensuring modules match the current running kernel version automatically.
- **Manual build and DaemonSet deployment (Driver Toolkit approach):** High maintenance burden, as module compatibility must be manually verified and re-deployed on every kernel update or cluster upgrade.

**Decision**
#TODO: Document the decision for each cluster.#

**Agreeing Parties**

- Person: #TODO#, Role: Enterprise Architect
- Person: #TODO#, Role: OCP Platform Owner
- Person: #TODO#, Role: AI/ML Platform Owner

## OCP-BM-04

**Title**
Root File System Encryption and Automated Unlock Mechanism

**Architectural Question**
If disk encryption (LUKS) is required for the bare metal nodes, which key management mechanism will be used to enable automated unlocking of the RHCOS root volume upon node boot?

**Issue or Problem**
Bare metal servers often require full disk encryption for security compliance. Without an automated mechanism, nodes cannot reboot unattended, which inhibits automated maintenance and recovery features.

**Assumption**
LUKS encryption is configured for the RHCOS root file system on bare metal nodes.

**Alternatives**

- TPM v2 Only Unlock (Policy-Based Decryption)
- TPM v2 and Tang Server Combination (Policy-Based Decryption)

**Justification**

- **TPM v2 Only Unlock (Policy-Based Decryption):** This uses the Trusted Platform Module (TPM) chip on the host to seal the decryption key, ensuring the key is released only if the boot measurement is correct. This requires no external infrastructure dependency for unlocking.
- **TPM v2 and Tang Server Combination (Policy-Based Decryption):** This method uses a network-bound key release (Tang) in addition to TPM measurements, allowing recovery of the system even if the TPM measurements change (e.g., BIOS upgrade). The security threshold can be customized, requiring a subset of available Tang servers plus the local TPM to decrypt the root volume.

**Implications**

- **TPM v2 Only Unlock (Policy-Based Decryption):** Simplest configuration, but node recovery after expected changes (like firmware updates that break TPM measurements) may require manual intervention.
- **TPM v2 and Tang Server Combination (Policy-Based Decryption):** Requires deployment and maintenance of external Tang server infrastructure (highly available). Offers greater flexibility in node recovery and resilience against unintended TPM measurement changes.

**Decision**
#TODO: Document the decision for each cluster.#

**Agreeing Parties**

- Person: #TODO#, Role: Enterprise Architect
- Person: #TODO#, Role: Security Expert
- Person: #TODO#, Role: Storage Expert

## OCP-BM-05

**Title**
Small Footprint HA Bare Metal Cluster Topology (TP)

**Architectural Question**
For bare metal deployments requiring high availability with minimal physical infrastructure, what specialized two-node topology will be selected?

**Issue or Problem**
Traditional Highly Available (HA) clusters require a minimum of three control plane nodes, increasing hardware costs for smaller deployments. OpenShift offers Technology Preview methods to achieve HA with only two main nodes on bare metal.

**Assumption**
The cluster topology is two nodes cluster.

**Alternatives**

- Two-Node Cluster with Fencing (TP)
- Two-Node Cluster with Arbiter (TP)

**Justification**

- **Two-Node Cluster with Fencing (TP):** This setup uses two control plane nodes and relies on fencing mechanisms (e.g., BMC access defined in `install-config.yaml`) to ensure data integrity by isolating a failed node. This minimizes node count to two actual worker/master nodes.
- **Two-Node Cluster with Arbiter (TP):** This setup uses two control plane nodes and an additional lightweight arbiter node (running only the arbiter component) to maintain quorum, effectively requiring three nodes in total (2 control + 1 arbiter).

**Implications**

- **Two-Node Cluster with Fencing (TP):** Requires robust configuration of BMC credentials and Redfish/IPMI access for fencing in the `install-config.yaml`. This is a Technology Preview feature.
- **Two-Node Cluster with Arbiter (TP):** Requires provisioning and maintaining a third, albeit small, arbiter node instance. This is a Technology Preview feature.

**Decision**
#TODO: Document the decision for each cluster.#

**Agreeing Parties**

- Person: #TODO#, Role: Enterprise Architect
- Person: #TODO#, Role: Network Expert
- Person: #TODO#, Role: OCP Platform Owner
