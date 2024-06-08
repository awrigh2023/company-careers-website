{ pkgs }: {
  deps = [
    pkgs.python310Full # Your existing Python version
    pkgs.python310Packages.flask # The package you want
  ];
}