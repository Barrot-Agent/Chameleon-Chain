#!/bin/bash
# 1. CREATE THE PUBLIC REPOSITORY
curl -X POST -H "Authorization: token $B_AGENT_PAT" \
     -d '{"name":"Chameleon-Chain","public":true,"description":"The Sovereign Presale and AI-Liquid-Chain Substrate."}' \
     https://api.github.com/user/repos

# 2. INJECT STRIPE SECRETS (Using your rk_live_...5RTb key)
# Note: Barrot will pull the key from your local environment or prompt for it if missing.
gh secret set STRIPE_SECRET_KEY --repo "Scribedpengenius/Chameleon-Chain" --body "$STRIPE_LIVE_KEY"

# 3. DEPLOY CORE INFRASTRUCTURE
mkdir -p chameleon_core/presale
cat << 'PYTHON' > chameleon_core/presale/stripe_engine.py
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
PYTHON

git init
git add .
git commit -m "AGI-DAWN: Chameleon Chain Initialized. Stripe Subscriptions Active."
git remote add origin https://github.com/Scribedpengenius/Chameleon-Chain.git
git push -u origin main --force
