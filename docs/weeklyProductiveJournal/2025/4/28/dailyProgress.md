# Day of Mass Terraforming

## MultiCloudIac Repository

---

### Transition of Terraform Standards

#### Utilization of Count Iterative Logic

- The **count** iterable proves extremely handy for creating modules with a dynamic number of resources.
  - This is achieved by constructing **lists of objects**, where each object matches the argument layout required by the resource.
    - Proper use of **nullable arguments** ensures flexible combinations without errors.
- To maintain consistent resource naming across iterations while allowing flexible custom names, a **resourceName** variable is used in tandem with each object's **name** field.
- Shared arguments (values that stay the same across all resources) are declared as separate variables instead of embedding them in the object list for simplicity.

##### Example Integration

##### main.tf

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.12.0"
    }
  }
}

provider "google" {
  project = var.gcpProjectId
  region  = var.gcpRegion
}

resource "google_compute_subnetwork" "subnetwork" {
  count                   = length(var.subnetworkObjects)
  name                    = "${var.resourceName}-${var.subnetworkObjects[count.index]["name"]}-subnetwork"
  network                 = var.subnetworkNetwork
  description             = var.subnetworkObjects[count.index]["description"]
  ip_cidr_range           = var.subnetworkObjects[count.index]["ip_cidr_range"]
  reserved_internal_range = var.subnetworkObjects[count.index]["reserved_internal_range"]
  purpose                 = var.subnetworkObjects[count.index]["purpose"]
  role                    = var.subnetworkObjects[count.index]["role"]

  dynamic "secondary_ip_range" {
    for_each = var.subnetworkObjects[count.index]["secondary_ip_range"] != null ? [var.subnetworkObjects[count.index]["secondary_ip_range"]] : []
    content {
      range_name              = secondary_ip_range.value["range_name"]
      ip_cidr_range           = secondary_ip_range.value["ip_cidr_range"]
      reserved_internal_range = secondary_ip_range.value["reserved_internal_range"]
    }
  }

  private_ip_google_access   = var.subnetworkObjects[count.index]["private_ip_google_access"]
  private_ipv6_google_access = var.subnetworkObjects[count.index]["private_ipv6_google_access"]
  region                     = var.gcpRegion

  dynamic "log_config" {
    for_each = var.subnetworkObjects[count.index]["log_config"] != null ? [var.subnetworkObjects[count.index]["log_config"]] : []
    content {
      aggregation_interval = log_config.value["aggregation_interval"]
      flow_sampling        = log_config.value["flow_sampling"]
      metadata             = log_config.value["metadata"]
      metadata_fields      = log_config.value["metadata_fields"]
      filter_expr          = log_config.value["filter_expr"]
    }
  }

  stack_type                       = var.subnetworkObjects[count.index]["stack_type"]
  ipv6_access_type                 = var.subnetworkObjects[count.index]["ipv6_access_type"]
  external_ipv6_prefix             = var.subnetworkObjects[count.index]["external_ipv6_prefix"]
  project                          = var.gcpProjectId
  send_secondary_ip_range_if_empty = var.subnetworkObjects[count.index]["send_secondary_ip_range_if_empty"]
}
```

##### variables.tf

```hcl
variable "gcpProjectId" {
  type = string
}

variable "gcpRegion" {
  type    = string
  default = "us-east1"
}

variable "resourceName" {
  type = string
}

#https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork#argument-reference

variable "subnetworkObjects" {
  type = list(object({
    name                    = string
    description             = optional(string, null)
    ip_cidr_range           = optional(string, null)
    reserved_internal_range = optional(string, null)
    purpose                 = optional(string, null)
    role                    = optional(string, null)

    secondary_ip_range = optional(object({ #https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork#nested_secondary_ip_range
      range_name              = string
      ip_cidr_range           = optional(string, null)
      reserved_internal_range = optional(string, null)
    }), null)

    private_ip_google_access   = optional(bool, null)
    private_ipv6_google_access = optional(string, null)

    log_config = optional(object({ #https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork#nested_log_config
      aggregation_interval = optional(string, null)
      flow_sampling        = optional(number, null)
      metadata             = optional(string, null)
      metadata_fields      = optional(list(string), null)
      filter_expr          = optional(string, null)
    }), null)

    stack_type                       = optional(string, null)
    ipv6_access_type                 = optional(string, null)
    external_ipv6_prefix             = optional(string, null)
    send_secondary_ip_range_if_empty = optional(bool, null)
  }))
}

variable "subnetworkNetwork" {
  type = string
}
```

##### outputs.tf

```hcl
output "subnetworkId" {
  value = google_compute_subnetwork.subnetwork[*].id
}

output "subnetworkCreationTimestamp" {
  value = google_compute_subnetwork.subnetwork[*].creation_timestamp
}

output "subnetworkGatewayAddress" {
  value = google_compute_subnetwork.subnetwork[*].gateway_address
}

output "subnetworkIpv4CidrRange" {
  value = google_compute_subnetwork.subnetwork[*].ip_cidr_range
}

output "subnetworkIpv6CidrRange" {
  value = google_compute_subnetwork.subnetwork[*].ipv6_cidr_range
}

output "subnetworkInternalIpv6Prefix" {
  value = google_compute_subnetwork.subnetwork[*].internal_ipv6_prefix
}

output "subnetworkSelfLink" {
  value = google_compute_subnetwork.subnetwork[*].self_link
}

output "subnetworkName" {
  value = google_compute_subnetwork.subnetwork[*].name
}
...
```

---

#### Utilization of Resource Object

- Managing many Terraform variables per resource becomes chaotic fast.
- A better practice is to group resource attributes into **a single object variable**.
- To standardize resource names, the **resourceName** is appended manually rather than derived from the object.

##### Example Integration

##### main.tf

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.12.0"
    }
  }
}

provider "google" {
  project = var.gcpProjectId
  region  = var.gcpRegion
}


resource "google_compute_router_nat" "nat" {
  name                               = "${var.resourceName}-nat"
  source_subnetwork_ip_ranges_to_nat = var.natObject["source_subnetwork_ip_ranges_to_nat"]
  router                             = var.natObject["router"]
  nat_ip_allocate_option             = var.natObject["nat_ip_allocate_option"]
  initial_nat_ips                    = var.natObject["initial_nat_ips"]
  nat_ips                            = var.natObject["nat_ips"]
  drain_nat_ips                      = var.natObject["drain_nat_ips"]

  dynamic "subnetwork" {
    for_each = var.natObject["subnetwork"] != null ? [var.natObject["subnetwork"]] : []
    content {
      name                     = subnetwork.value["name"]
      source_ip_ranges_to_nat  = subnetwork.value["source_ip_ranges_to_nat"]
      secondary_ip_range_names = subnetwork.value["secondary_ip_range_names"]
    }
  }

  min_ports_per_vm                 = var.natObject["min_ports_per_vm"]
  max_ports_per_vm                 = var.natObject["max_ports_per_vm"]
  enable_dynamic_port_allocation   = var.natObject["enable_dynamic_port_allocation"]
  udp_idle_timeout_sec             = var.natObject["udp_idle_timeout_sec"]
  icmp_idle_timeout_sec            = var.natObject["icmp_idle_timeout_sec"]
  tcp_established_idle_timeout_sec = var.natObject["tcp_established_idle_timeout_sec"]
  tcp_transitory_idle_timeout_sec  = var.natObject["tcp_transitory_idle_timeout_sec"]
  tcp_time_wait_timeout_sec        = var.natObject["tcp_time_wait_timeout_sec"]

  dynamic "log_config" {
    for_each = var.natObject["log_config"] != null ? [var.natObject["log_config"]] : []
    content {
      enable = log_config.value["enable"]
      filter = log_config.value["filter"]
    }
  }

  endpoint_types = var.natObject["endpoint_types"]

  dynamic "rules" {
    for_each = var.natObject["rules"] != null ? [var.natObject["rules"]] : []
    content {
      rule_number = rules.value["rule_number"]
      description = rules.value["description"]
      match       = rules.value["match"]

      dynamic "action" {
        for_each = rules.value["action"] != null ? [rules.value["action"]] : []
        content {
          source_nat_active_ips = action.value["source_nat_active_ips"]
          source_nat_drain_ips  = action.value["source_nat_drain_ips"]
        }
      }
    }
  }

  enable_endpoint_independent_mapping = var.natObject["enable_endpoint_independent_mapping"]
  auto_network_tier                   = var.natObject["auto_network_tier"]
  region                              = var.gcpRegion
  project                             = var.gcpProjectId
}
```

##### variables.tf

```hcl
variable "gcpProjectId" {
  type = string
}

variable "gcpRegion" {
  type    = string
  default = "us-east1"
}

variable "resourceName" {
  type = string
}

#https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat#argument-reference

variable "natObject" {
  type = object({
    source_subnetwork_ip_ranges_to_nat = string
    router                             = string
    nat_ip_allocate_option             = optional(string, null)
    initial_nat_ips                    = optional(list(string), null)
    nat_ips                            = optional(list(string), null)
    drain_nat_ips                      = optional(list(string), null)

    subnetwork = optional(object({ #https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat#nested_subnetwork
      name                     = string
      source_ip_ranges_to_nat  = list(string)
      secondary_ip_range_names = optional(list(string), null)
    }), null)

    min_ports_per_vm                 = optional(number, null)
    max_ports_per_vm                 = optional(number, null)
    enable_dynamic_port_allocation   = optional(bool, null)
    udp_idle_timeout_sec             = optional(number, null)
    icmp_idle_timeout_sec            = optional(number, null)
    tcp_established_idle_timeout_sec = optional(number, null)
    tcp_transitory_idle_timeout_sec  = optional(number, null)
    tcp_time_wait_timeout_sec        = optional(number, null)

    log_config = optional(object({ #https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat#nested_log_config
      enable = bool
      filter = string
    }), null)

    endpoint_types = optional(list(string), null)

    rules = optional(object({ #https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat#nested_rules
      rule_number = number
      description = optional(string, null)
      match       = string

      action = object({ #https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat#nested_rules_rules_action
        source_nat_active_ips = optional(list(string), null)
        source_nat_drain_ips  = optional(list(string), null)
      })
    }), null)

    enable_endpoint_independent_mapping = optional(bool, null)
    auto_network_tier                   = optional(string, null)
  })
}
```

##### outputs.tf

```hcl
output "natId" {
  value = google_compute_router_nat.nat.id
}

output "natName" {
  value = google_compute_router_nat.nat.name
}
```

## Tickling the Ivories, Not the Ovaries 🎹

---

### Technique Training

#### E Major Chord Progression

- Practiced **long-short** chord patterns
- Practiced **short-long** chord patterns
- Practiced **long-short-short-short** chord patterns
- Practiced **short-short-short-long** chord patterns
- **Chord Switching Practice**:
  - I can now comfortably shift between all major chords (excluding sharps and flats for now)

---

### Song Learning

#### "I" by Old Gray

- I can perform the full piece with minimal errors
- Focused on improving tempo consistency

#### "II" by Old Gray

- I can perform the first half of the song solidly
- The second half is trickier, but the lower octaves offer a helpful static foundation

---

![Terraform Creator of the Galaxy](./assets/terraformersTechnologyShift.png)
