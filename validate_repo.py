#!/usr/bin/env python3
import json
import os
import sys

def validate():
    errors = []

    if not os.path.exists("index.json"):
        errors.append("index.json missing")
        return errors

    try:
        with open("index.json") as f:
            index = json.load(f)
    except Exception as e:
        errors.append(f"Invalid index.json JSON syntax: {e}")
        return errors

    if index.get("schema_version") != 1:
        errors.append("index.json schema_version must be 1")

    packages = index.get("packages")
    if not isinstance(packages, dict):
        errors.append("index.json packages field must be a dictionary")
        return errors

    for pkg_id, entry in packages.items():
        def_path = entry.get("definition")
        pkg_type = entry.get("type")

        if not def_path:
            errors.append(f"Package '{pkg_id}' in index missing definition path")
            continue
        if pkg_type not in ["binary", "source"]:
            errors.append(f"Package '{pkg_id}' in index has invalid type '{pkg_type}'")

        if not os.path.exists(def_path):
            errors.append(f"Package definition file '{def_path}' for '{pkg_id}' does not exist")
            continue

        try:
            with open(def_path) as f:
                pkg_def = json.load(f)
        except Exception as e:
            errors.append(f"Invalid JSON syntax in '{def_path}': {e}")
            continue

        if pkg_def.get("schema_version") != 1:
            errors.append(f"'{def_path}' schema_version must be 1")
        if pkg_def.get("id") != pkg_id:
            errors.append(f"'{def_path}' id '{pkg_def.get('id')}' does not match key '{pkg_id}'")
        if pkg_def.get("type") != pkg_type:
            errors.append(f"'{def_path}' type '{pkg_def.get('type')}' does not match index type '{pkg_type}'")
        if not pkg_def.get("name"):
            errors.append(f"'{def_path}' missing 'name'")
        if not pkg_def.get("version"):
            errors.append(f"'{def_path}' missing 'version'")

        if pkg_type == "binary":
            downloads = pkg_def.get("downloads")
            if not isinstance(downloads, dict) or not downloads:
                errors.append(f"'{def_path}' (binary) must have non-empty 'downloads' dictionary")
            else:
                for platform, dl in downloads.items():
                    if not dl.get("url"):
                        errors.append(f"'{def_path}' download for '{platform}' missing 'url'")
        elif pkg_type == "source":
            source = pkg_def.get("source")
            build = pkg_def.get("build")
            if not isinstance(source, dict):
                errors.append(f"'{def_path}' (source) missing 'source' object")
            if not isinstance(build, dict):
                errors.append(f"'{def_path}' (source) missing 'build' object")

    return errors

if __name__ == "__main__":
    errs = validate()
    if errs:
        print("Validation errors found:")
        for err in errs:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("Validation succeeded! Repository structure and package schemas are valid.")
