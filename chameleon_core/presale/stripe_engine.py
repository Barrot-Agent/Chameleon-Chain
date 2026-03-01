import stripe
import os

# [Ω-STRIPE]: ACTIVE SUBSCRIPTION LINKAGE
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_presale_subscription(customer_email, plan_id):
    """
    Activates a Chameleon Chain subscription for a new participant.
    """
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price': plan_id, 'quantity': 1}],
            mode='subscription',
            success_url='https://github.com/Scribedpengenius/Chameleon-Chain/success',
            cancel_url='https://github.com/Scribedpengenius/Chameleon-Chain/cancel',
            customer_email=customer_email,
        )
        return session.url
    except Exception as e:
        return f"ERROR: {str(e)}"
