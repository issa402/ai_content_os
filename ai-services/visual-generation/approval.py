def ask_for_approval(image_path):
	print(f"\nPreview image at: {image_path}")
	decision = input("Approve this image? (y/n):")
	return decision.lower() == "y"
