resource "helm_release" "simple_elasticsearch_cleaner" {
  namespace = var.namespace
  name      = "simple-elasticsearch-cleaner"
  chart     = "${path.module}/../helm-charts/simple-elasticsearch-cleaner"

  set {
    name  = "image.tag"
    value = var.image_tag
  }

  set {
    name  = "image.pullPolicy"
    value = var.image_pull_policy
  }

  set {
    name  = "namespace"
    value = var.namespace
  }

  set {
    name  = "schedule"
    value = var.schedule
  }

  set {
    name  = "number_of_days"
    value = var.number_of_days
  }

  set {
    name  = "resources.limits.cpu"
    value = var.resources_limits_cpu
  }

  set {
    name  = "resources.limits.memory"
    value = var.resources_limits_memory
  }

  set {
    name  = "resources.requests.cpu"
    value = var.resources_requests_cpu
  }

  set {
    name  = "resources.requests.memory"
    value = var.resources_requests_memory
  }

  dynamic "set" {
    for_each = var.node_selector

    content {
      name  = "nodeSelector.${replace(set.key, ".", "\\.")}"
      value = set.value
    }
  }
}
