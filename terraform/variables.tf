variable "image_tag" {
  default = "2.1.0"
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

variable "es_port" {
  default = "9200"
}

variable "secrets_host_name" {
  default = "simple-elasticsearch-cleaner-secret"
}

variable "secrets_host_key" {
  default = "elasticsearch-host"
}

variable "secrets_user_name" {
  default = "elasticsearch-credentials"
}

variable "secrets_user_key" {
  default = "elasticsearch-username"
}

variable "secrets_password_name" {
  default = "elasticsearch-credentials"
}

variable "secrets_password_key" {
  default = "elasticsearch-password"
}
