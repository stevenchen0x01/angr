import simuvex

######################################
# abort
######################################

class abort(simuvex.SimProcedure):
    NO_RET = True

    def run(self):
        return
