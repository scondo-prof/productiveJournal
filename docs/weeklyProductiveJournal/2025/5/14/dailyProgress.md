# Day of Multiple Identities

## AWS

### Power of the ALB

ALBs are rather useful when it comes to multiple types of infrastructure implimentations. The one this will touch on is the ability to have microservices across multiple EC2s, Multiple Services on The Same EC2, or Both Simultaneously

#### Listeners

The first topic I will touch on are listeners. They are good at directing traffic that is coming into the load balancer. For instance say the Load Balancer has a listener on port 443 due to an SSL being tied to the ALB (perhaps from ACM). Rules can be applied to the Listener to direct traffic based on a variety of factors. For instance in a recent integration I had listener rules look for particular urls in the headers. I tied the ALBs Domain to 2 different CName records. These CName records had 2 different wildcard domain names for instance test-jenkins.test.com and test-app.test.com. Both values of the CName records were the domain name of the ALB.

From there, I added 2 listener rules for port 443 besides default, 1 rule that looked for test-jenkins.test.com in the header and one that looked for test-app.test.com in the headers. From there each rule directed traffic to its complimenting target group.

#### Target Groups

These state which port to expect traffic from, it then has you select a target, for this example I used EC2 instances as the target. For example my jenkins service I created a target group called target jenkins. My Jenkins Service lives on port 8080. Thus I put the protocol port to 8080. I then selected the EC2 insstance Jenkins is live on as my target instance, and selected the target port of that server as 8080(the port jenkins is on.) This target was then assigned as the destination to the Listener Rule declared above. I repeated the same steps for the test-app target/listener relationship.

#### Hide within Private Subnets

Cool thing about this integration is the EC2s can live within a private subnet. For Egress traffic(if the service needs to talk with the internet) could be directed through a NAT Gateway with a Static IP that lives in a public subnet within the same VPC. While Egress traffic is handled by the ALB that lives in a public subnet in the Same VPC. This works with corresponding Routes allowing traffic, and security groups allowing traffic from specific ports. For intance, the security group that is attached to the jenkins server, needs to have an ingress rule that allows traffic on port 8080 from the ALBs security group. Practically saying I am allowing traffic through our VPCs network from the ALB.
