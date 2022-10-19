source settings/variables.txt
firebase_real_time_db_url="${{ secrets.FIREBASE_DB_URL }}"

function run_tests() {
  python3 "$test_file"
  git add logs/tests_results.txt
}

function extract_grades() {
  python3 -m classroom_tools.grading.create_grades \
    --test_associations_path="$test_associations_path"
  git add logs/grades.json
}

function show_grades() {
  python3 -m classroom_tools.grading.show_grades_in_readme
  git add README.md
}

function push_modifications() {
  git config --local user.email "action@github.com"
  git config --local user.name "GitHub Action"
  git commit -a -m "Updated autograding results"
  git pull -v --rebase=true
  git push -v
}

function patch_db() {
  python3 -m classroom_tools.grading.patch_db \
    --access_token="" \
    --firebase_real_time_db_url="$firebase_real_time_db_url" \
    --github_repo="$(basename $(pwd))"
}

if [[ $GITHUB_REPOSITORY =~ $org_name/$repo_filter ]]
then
  python3 -m pip install -q setuptools
  python3 -m pip install -q git+"$classroom_tools_url"
  run_tests
  extract_grades
  show_grades
  push_modifications
  patch_db
else
  exit 1
fi
