{{- define "secret.name" -}}
  {{ .Release.Name }}-secret
{{- end -}}

{{- define "configMap.name" -}}
  {{ .Release.Name }}-config-map
{{- end -}}

{{- define  "createx.deployment.name" -}}
  {{ .Release.Name }}-deployment
{{- end -}}

{{- define "createx.service.name" -}}
  {{ .Values.createx.appName }}-service
{{- end -}}

{{- define "createx.port" -}}
  8000
{{- end -}}

{{- define  "createx.pvc.name" -}}
  {{ .Release.Name }}-pvc
{{- end -}}

{{- define "tex-engine.labels" -}}
  app: "tex-engine"
{{- end -}}

{{- define "tex-engine.deployment.name" -}}
  tex-engine-deployment
{{- end -}}

{{- define "tex-engine.service.name" -}}
  tex-engine-service
{{- end -}}

{{- define "tex-engine.port" -}}
  5000
{{- end -}}

{{- define "tex-engine.protocol" -}}
  http
{{- end -}}

{{- define "tex-engine.url" -}}
  {{ include "tex-engine.protocol" . }}://{{ include "tex-engine.service.name" . }}:{{ include "tex-engine.port" . }}
{{- end -}}
