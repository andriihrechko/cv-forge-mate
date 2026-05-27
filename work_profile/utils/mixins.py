from django.utils import timezone


class DateValidationMixin:
    def clean(self):
        cleaned_data = super().clean()
        started_at = cleaned_data.get("started_at")
        ended_at = cleaned_data.get("ended_at")
        today = timezone.now().date()
        if started_at and started_at > today:
            self.add_error("started_at", "Start date cannot be in the future.")
        if ended_at and ended_at > today:
            self.add_error("ended_at", "End date cannot be in the future.")
        if started_at and ended_at and ended_at < started_at:
            self.add_error(
                "ended_at", "End date cannot be earlier than the start date."
            )
        return cleaned_data


class ProfileOwnerMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not self.object:
            kwargs["instance"] = self.model(
                profile=self.request.user.workprofile
            )
        return kwargs
