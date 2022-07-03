def get_results(event_name, write):

  results_message = f"Current {event_name.lower().capitalize()} results:\n"
  for x in range (len(write)):
    results_message = f"{results_message}\n{x+1}. **{write[x][0]}** Ao5: {write[x][6]}".replace("'", "")
  return results_message