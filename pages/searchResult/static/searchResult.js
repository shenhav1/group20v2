document.addEventListener("DOMContentLoaded", () => {
	const therapistButtons = document.querySelectorAll(".therapist button");

	therapistButtons.forEach((button) => {
		button.addEventListener("click", () => {
			const therapistName = button.id;

			fetch("/set_therapist_name", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({ name: therapistName }),
			})
				.then((response) => {
					if (response.ok) {
						window.location.href = "/profile";
					} else {
						console.error(
							"Failed to set therapist name in session"
						);
					}
				})
				.catch((error) => {
					console.error("Error:", error);
				});
		});
	});
});
