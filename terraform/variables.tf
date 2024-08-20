variable "image_tag" {
  default = "latest"
}

variable "image_pull_policy" {
  default = "Always"
}

variable "namespace" {
  default = "elasticsearch"
}

variable "schedule" {
  default = "0 1 * * *" # At 01:00 every day
}

variable "number_of_days" {
  default = "30"
}

variable "resources_limits_cpu" {
  default = "200m"
}

variable "resources_limits_memory" {
  default = "256Mi"
}

variable "resources_requests_cpu" {
  default = "100m"
}

variable "resources_requests_memory" {
  default = "128Mi"
}

variable "node_selector" {
  default = {}
}
