variable "redshift_username" {
  description = "Master username for Redshift"
  type        = string
  default     = "admin"
}

variable "redshift_password" {
  description = "Master password for Redshift"
  type        = string
  sensitive   = true
}
