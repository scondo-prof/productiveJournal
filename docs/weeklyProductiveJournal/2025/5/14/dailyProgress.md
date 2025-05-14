# Day of Multiple Identities

## AWS

### Harnessing Application Load Balancers

Application Load Balancers (ALBs) enable flexible routing for microservices architectures, allowing multiple services across one or more EC2 instances to coexist behind a single endpoint.

#### Listeners and Routing Rules

Listeners define the ports and protocols on which the ALB accepts incoming traffic (e.g., HTTPS on port 443). You can attach rules to a listener to direct requests based on host headers, path patterns, or HTTP methods:

- **Host‑based routing**: Inspect the `Host` header and forward to different target groups. For example, traffic for `test-jenkins.example.com` and `test-app.example.com` can share the same ALB DNS, with separate listener rules:

  1. Rule matching `Host = test-jenkins.example.com` → forward to **jenkins-tg**
  2. Rule matching `Host = test-app.example.com` → forward to **app-tg**

- **Path‑based routing**: Route `/api/*` to one service and `/ui/*` to another.

These capabilities eliminate the need for multiple load balancers and simplify DNS management via CNAME records pointing to the ALB’s DNS name.

#### Target Groups and Health Checks

A target group associates a set of compute resources (e.g., EC2 instances or IPs) with a protocol and port:

- **Protocol & port**: Specify `HTTP:8080` for Jenkins or `HTTP:80` for your web app.
- **Health checks**: Configure an HTTP path (e.g., `/health`) and thresholds to ensure only healthy instances receive traffic.

Once defined, each listener rule forwards matching requests to its designated target group.

#### Private Subnets and Secure Networking

To keep backend instances off the public internet:

1. **Private subnets** host your EC2 services.
2. **NAT Gateway** in a public subnet provides outbound internet access (for software updates, etc.) while preserving a static egress IP.
3. **ALB in public subnets** handles all ingress traffic and forwards it internally.
4. **Security Groups** enforce least‑privilege access:

   - ALB SG allows inbound HTTPS (443) from the internet
   - EC2 SG allows inbound from the ALB SG on the service port (e.g., 8080)

This design ensures that all external traffic passes through the ALB, then into private subnets under strict security rules.

---

## Tickling the Ivories, Not the Ovaries

### Song Practice

#### "II" by Old Gray

I can now perform the entire arrangement smoothly at a moderate tempo. Occasional missed notes highlight areas for further finger positioning drills.

#### Michael Myers’ Theme

I’ve mastered the first eight measures, focusing on the iconic minor chords. Next, I’ll work on the transition into the descending motif while maintaining the brisk tempo and articulation accuracy.

> _Why are pianos so hard to open?_

> _The keys are inside._

---

![Organization and Creativity](./assets/organizationAndCreativity.png)
