# Day of Video Clarity

## The Video Smoother

### AWS

#### EC2 Quota Increase

I submitted an AWS service-quota request and received approval: my account can now use up to **84 G-series vCPUs** simultaneously. In AWS parlance, “84 Computers” equates to 84 virtual CPUs across G-series instances. This boost ensures we have ample compute power, memory, and GPU resources to render and export large Adobe Premiere projects without bottlenecks.

#### Project Delivery

- **Rendered & Uploaded:** Completed the final cut of `Loons @ Moose Pond` and added it to our YouTube channel: [Loons @ Moose Pond](https://youtu.be/LBpmwUC6fcc?si=NSe4k5_Nft4BXHd6).
- **Performance Gains:** With the increased vCPU quota, export times dropped by over 30%, and GPU-accelerated effects now run smoothly.

> **Next Steps:**
>
> 1. Benchmark render times across different G-series instance sizes to find the optimal balance of cost vs performance.
> 2. Automate spin-up/down of EC2 instances via Terraform and Lambda to minimize idle cost.
> 3. Explore AWS Thinkbox Deadline or AWS MediaConvert for managed rendering workflows. (Is it worth the price/ time to learn?)
