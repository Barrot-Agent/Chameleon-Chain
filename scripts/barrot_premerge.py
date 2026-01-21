import os
import subprocess

def ensure_gitlab_ci():
    ci_path = ".gitlab-ci.yml"
        if os.path.exists(ci_path):
                print("🧾 .gitlab-ci.yml already exists. Barrot will not overwrite it.")
                        return False

                            content = """stages:
                              - test

                              barrot_premerge:
                                stage: test
                                  script:
                                      - python3 scripts/barrot_premerge.py
                                        only:
                                            - merge_requests
                                            """
                                                with open(ci_path, "w") as f:
                                                        f.write(content)
                                                            print("🛠️  Barrot created .gitlab-ci.yml")
                                                                return True

                                                                def git_push_ci_update():
                                                                    try:
                                                                            subprocess.run(["git", "add", ".gitlab-ci.yml"], check=True)
                                                                                    subprocess.run(["git", "commit", "-m", "Barrot: CI pipeline initialized"], check=True)
                                                                                            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
                                                                                                    print("🚀 Barrot pushed the updated .gitlab-ci.yml to GitLab.")
                                                                                                        except subprocess.CalledProcessError as e:
                                                                                                                print(f"❌ Git push failed: {e}")

                                                                                                                def main():
                                                                                                                    created = ensure_gitlab_ci()
                                                                                                                        if created:
                                                                                                                                git_push_ci_update()
                                                                                                                                    print("✅ Barrot pre-merge complete.")

                                                                                                                                    if __name__ == "__main__":
                                                                                                                                        main()
                                                                                                                                        